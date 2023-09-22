import copy
from xml.etree.ElementTree import ElementTree, Element
from mapper import SVGRoot, SVGElement, SVGImage, SVGCollection
from mapper.to_svg_mapper import IMAGE_TAG


def merge_svg_root_and_element_tree(root: SVGRoot, etree: ElementTree) -> ElementTree:
    copied_etree = copy.deepcopy(etree)
    for svg_child, etree_child in zip(root, copied_etree.getroot()):
        merge_svg_and_element(svg_child, etree_child)
    return copied_etree


def merge_svg_and_element(svg_element: SVGElement, element: Element) -> Element:
    if isinstance(svg_element, SVGCollection):
        return merge_svg_collection_and_element(svg_element, element)
    if isinstance(svg_element, SVGImage):
        return merge_svg_image_and_element(svg_element, element)
    return element


def merge_svg_collection_and_element(
        svg_collection: SVGCollection, element: Element
) -> Element:
    merged_children = [
        merge_svg_and_element(svg_child_element, child_element)
        for svg_child_element, child_element in zip(svg_collection, element)
    ]
    element.clear()
    element.extend(merged_children)
    return element



def merge_svg_image_and_element(svg_image: SVGImage, element: Element) -> Element:
    if element.tag != IMAGE_TAG:
        return element
    element.set("href", svg_image.get_href())
    return element
